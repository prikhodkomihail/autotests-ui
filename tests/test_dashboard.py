from pages.dashboard_page import DashboardPage
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_wih_state: DashboardPage):
    dashboard_page_wih_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    dashboard_page_wih_state.navbar.check_visible('username')
    dashboard_page_wih_state.sidebar.check_visible()
    
    dashboard_page_wih_state.toolbar_view.check_visible()
    dashboard_page_wih_state.scores_chart_view.check_visible('Scores')
    dashboard_page_wih_state.courses_chart_view.check_visible('Courses')
    dashboard_page_wih_state.students_chart_view.check_visible('Students')
    dashboard_page_wih_state.activities_chart_view.check_visible('Activities')