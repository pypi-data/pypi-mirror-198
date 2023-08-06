#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

from app.api import Api
from app.application import Application
from app.internal.login import login
from app.logz import create_logger
from app.public.cisa import alerts, update_known_vulnerabilities, update_regscale
from app.utils.regscale_utils import get_all_from_module
import pytest


class Test_Cisa:
    logger = create_logger()
    app = Application()
    api = Api(app)

    def test_init(self):
        with open("init.yaml", "r") as f:
            data = f.read()
            self.logger.debug("init file: %s", data)
            assert len(data) > 5

    def test_login(self):
        app = Application()
        self.logger.debug(os.getenv("REGSCALE_USER"))
        self.logger.debug(os.getenv("REGSCALE_PASSWORD"))

        jwt = login(os.getenv("REGSCALE_USER"), os.getenv("REGSCALE_PASSWORD"), app=app)
        self.logger.info(jwt)
        assert jwt is not None

    def test_kev(self):
        data = update_known_vulnerabilities()
        assert data
        update_regscale(data)

    def test_updates(self):
        reg_threats = get_all_from_module(api=self.api, module="threats")
        assert reg_threats

    @pytest.mark.skip(
        reason="Alerts page has been redesigned, skipping until this can be addressed."
    )
    def test_alerts(self):
        alerts(2020)
