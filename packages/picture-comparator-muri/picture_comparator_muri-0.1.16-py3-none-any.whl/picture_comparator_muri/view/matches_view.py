import random
from dataclasses import dataclass
from typing import Union, Optional, Dict, Tuple, Sequence

from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt, QSize
from PySide6.QtGui import QPainter, QImage, QTransform, QPixmap, QResizeEvent
from PySide6.QtWidgets import QListView, QAbstractItemDelegate, QStyleOptionViewItem, QStyle, QWidget, QAbstractItemView

from picture_comparator_muri.model.image_group import ImageGroup
from picture_comparator_muri.model.watched_list import WatchedList, WatchedListModel


@dataclass
class ImageArrangement:
    size: float
    positions: Sequence[Tuple[float, float]]


class ListMatchDelegate(QAbstractItemDelegate):
    MATCH_SIZE = 150
    ROTATE_MIN = -15
    ROTATE_MAX = 15

    BACKGROUND_COLORS = (0xFFFFFFFF, 0xFFF6F6F6)

    ARRANGEMENT = {
        2: ImageArrangement(.75, ((.33, .33), (.66, .66))),
        3: ImageArrangement(.5, ((.25, .25), (.75, .25), (.5, .75))),
        4: ImageArrangement(.5, ((.25, .25), (.75, .25), (.25, .75), (.75, .75)))
    }

    def __init__(self):
        super().__init__()
        self._cache: Dict = {}

    def _get_group_bitmap(self, index: Union[QModelIndex, QPersistentModelIndex]):
        image_group: ImageGroup = index.model().data(index, Qt.DisplayRole)
        pixmap = self._cache.get(image_group)
        if not pixmap:
            pixmap = QImage(self.MATCH_SIZE, self.MATCH_SIZE, QImage.Format_ARGB32)
            bcg_color: int = self.BACKGROUND_COLORS[index.row() % len(self.BACKGROUND_COLORS)]
            pixmap.fill(bcg_color)
            painter = QPainter(pixmap)

            visible_elements: int = len(image_group)
            visible_elements = min(4, visible_elements)
            arrangement: ImageArrangement = self.ARRANGEMENT[visible_elements]

            for i, image in enumerate(image_group[:4]):
                qimg = QPixmap(image.path)
                angle = random.uniform(self.ROTATE_MIN, self.ROTATE_MAX)
                transform = QTransform()
                transform.rotate(angle)
                rotated = qimg.transformed(transform, Qt.SmoothTransformation)
                if qimg.width() > qimg.height():
                    change_ratio = rotated.width() / qimg.width()
                    qimg = rotated.scaledToWidth(arrangement.size * self.MATCH_SIZE * change_ratio, Qt.SmoothTransformation)
                else:
                    change_ratio = rotated.height() / qimg.height()
                    qimg = rotated.scaledToHeight(arrangement.size * self.MATCH_SIZE * change_ratio, Qt.SmoothTransformation)

                x = arrangement.positions[i][0] * self.MATCH_SIZE - qimg.width() / 2
                y = arrangement.positions[i][1] * self.MATCH_SIZE - qimg.height() / 2
                painter.drawImage(x, y, qimg.toImage())
            self._cache[image_group] = pixmap
        return pixmap

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> None:
        pixmap = self._get_group_bitmap(index)
        painter.drawImage(option.rect.x(), option.rect.y(), pixmap)
        if option.state & QStyle.State_Selected:
            brush = option.palette.highlight()
            color = brush.color()
            color.setAlphaF(.6)
            brush.setColor(color)
            painter.fillRect(option.rect, color)

    def sizeHint(self, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]) -> QSize:
        pixmap = self._get_group_bitmap(index)
        return pixmap.size()

    def clear_cache(self):
        self._cache.clear()


class MatchesListView(QListView):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setModel(WatchedListModel())
        self.setItemDelegate(ListMatchDelegate())
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.base_width: Optional[int] = None  # Only set it after setupUi

    def model(self) -> WatchedListModel:  # Override type hint
        return super().model()

    def set_groups(self, groups: WatchedList):
        self.model().set_list(groups)

    def resizeEvent(self, e: QResizeEvent) -> None:
        super().resizeEvent(e)
        self.adjust_width_for_scroll()

    def adjust_width_for_scroll(self):
        # We assume the width was set during setupUi and should be fixed.
        if self.base_width is None:
            self.base_width = self.width()
        if self.verticalScrollBar().isVisible():
            self.setFixedWidth(self.base_width + self.verticalScrollBar().width())
        else:
            self.setFixedWidth(self.base_width)

    def itemDelegate(self) -> ListMatchDelegate:
        return super().itemDelegate()
