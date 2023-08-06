#
#  This file is part of IOCBIO Gel.
#
#  SPDX-FileCopyrightText: 2022-2023 IOCBIO Gel Authors
#  SPDX-License-Identifier: GPL-3.0-or-later
#


from sqlalchemy import select

from iocbio.gel.application.event_registry import EventRegistry
from iocbio.gel.command.history_manager import HistoryManager
from iocbio.gel.domain.measurement_lane import MeasurementLane
from iocbio.gel.repository.entity_repository import EntityRepository


class MeasurementLaneRepository(EntityRepository):
    def __init__(self, db, event_registry: EventRegistry, history_manager: HistoryManager):
        super().__init__(
            db,
            history_manager,
            event_registry,
            event_registry.measurement_lane_updated,
            event_registry.measurement_lane_added,
            event_registry.measurement_lane_deleted,
        )

    def fetch_by_measurement_id(self, measurement_id):
        stmt = (
            select(MeasurementLane)
            .where(MeasurementLane.measurement_id == measurement_id)
            .order_by(MeasurementLane.id)
        )

        return self.db.execute(stmt).scalars().all()
