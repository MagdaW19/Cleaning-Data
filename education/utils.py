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

"""Module with utility functions for cleaning data.
"""

def fix_census_date(x):
    """Utitlity function fixing the last census date in file with country info

    Parameters
    ----------
    x : str
        Year or Year with adnotations

    Returns
    -------
    str
        Year as string 
    """
    x = str(x)
    if x == "Guernsey: 2009; Jersey: 2011.":
        return "2009"
    elif len(x)>4:
        return x[:4]
    else:
        return x

def is_country(x):
    """Utility function checking if short name belongs to country or region/group """
    regions = ['Arab World',
                'East Asia & Pacific (developing only)',
                'East Asia & Pacific (all income levels)',
                'Europe & Central Asia (developing only)',
                'Europe & Central Asia (all income levels)',
                'Euro area',
                'European Union',
                'High income',
                'Heavily indebted poor countries (HIPC)',
                'Latin America & Caribbean (developing only)',
                'Latin America & Caribbean (all income levels)',
                'Least developed countries: UN classification',
                'Low income',
                'Lower middle income',
                'Low & middle income',
                'Middle East & North Africa (all income levels)',
                'Middle income',
                'Middle East & North Africa (developing only)',
                'North America',
                'OECD members',
                'South Asia',
                'Sub-Saharan Africa (developing only)',
                'Sub-Saharan Africa (all income levels)',
                'Upper middle income',
                'World']
    if x not in regions:
        return True
    else:
        return False

def simplify_indicators(ind):
    ind = ind.replace('Barro-Lee: ','')
    ind = ind.replace('Percentage', '%')
    ind = ind.replace('Average', 'Avg.')
    ind = ind.replace('Population','Pop.')
    ind = ind.replace('population','pop.')
    ind = ind.replace('. Completed Primary','')
    ind = ind.replace('. Completed Secondary','')
    ind = ind.replace('. Completed Tertiary','')
    return ind

