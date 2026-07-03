from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(title).to_be_visible()
        expect(title).to_have_text('Courses')

        text_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(text_block).to_be_visible()
        expect(text_block).to_have_text('There is no results')

        empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()

        result_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_block).to_be_visible()
        expect(result_block).to_have_text('Results from the load test pipeline will be displayed here')
