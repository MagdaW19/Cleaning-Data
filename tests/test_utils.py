# Copyright 2021 Magda Wójcicka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for testing utility functions for cleaning Education Stats data from data.worldbank.org."""
import unittest
from education import utils

class TestUtils(unittest.TestCase):
    def test_pop_census(self):
        self.assertEqual(utils.fix_census_date('1943'),'1943')
        self.assertEqual(utils.fix_census_date('2012. Population'),'2012')

    def test_is_country(self):
        self.assertEqual(utils.is_country('World'), False)
        self.assertEqual(utils.is_country('Poland'), True)

if __name__ == '__main__':
    unittest.main()