# AnyRepo
# Copyright (C) 2020  Anybox
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from anyrepo.models.log import Log


def test_log_into_db(app):
    with app.app_context():
        orig = Log.query.count()
        app.logger.error("This is a test")
        assert Log.query.count() >= orig + 1
        assert (
            Log.query.filter_by(level="ERROR", msg="This is a test").first()
            is not None
        )


def test_log_with_extra(app, dbapi):
    with app.app_context():
        app.logger.error("This is a second test", {"api_id": dbapi.id})
        assert (
            Log.query.filter_by(
                level="ERROR", msg="This is a second test", api_id=dbapi.id
            ).first()
            is not None
        )