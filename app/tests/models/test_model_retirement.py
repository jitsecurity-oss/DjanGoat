# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import Retirement
from app.tests.mixins import ModelCrudTests, Pep8ModelTests


class RetirementModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
    def setUp(self):

        # Create the user
        input_user_id = 1
        input_email = "ryan.dens@contrastsecurity.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        input_auth_token = "test"

        self.parent = User.objects.create(
            user_id=input_user_id,
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date, auth_token=input_auth_token
        )
        self.parent.save()

        # Create Retirement Model
        input_total = "102543"
        input_employer_contrib = "2543"
        input_employee_contrib = "100000"
        perf_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        perf_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.model = Retirement.objects.create(
            total=input_total,
            employer_contrib=input_employer_contrib,
            employee_contrib=input_employee_contrib,
            created_at=perf_input_create_date,
            updated_at=perf_input_update_date,
            user_id=self.parent,
        )
        self.model.save()

        # Model attributes to be updated
        self.attributes = ["user_id", "total", "employee_contrib",
                           "employer_contrib", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "102544"

        # Path for pep8 tests
        self.path = "app/models/Retirement/retirement.py"