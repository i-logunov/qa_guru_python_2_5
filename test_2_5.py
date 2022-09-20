import os.path

from selene import have
from selene.support.shared import browser


def test_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Ivan')
    browser.element('[id="lastName"]').type('Ivanov')
    browser.element('[id="userEmail"]').type('ivanov@qa.ru')
    browser.element('[class="custom-control-label"]').click()
    browser.element('[id="userNumber"]').type('9850001122')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="2001"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="4"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--011"]').click()
    browser.element('[id="subjectsInput"]').type('Ar').press_enter().type('B').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('resources/photo.jpg'))
    browser.element('[id="currentAddress"]').type('Russia\nMoscow\nRed Square\n1')
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').type('De').press_enter()
    browser.element('[id="submit"]').press_enter()

    dialog_table = browser.element('.modal-content').element('.table')
    rows = dialog_table.all('tbody tr')
    rows.should(have.texts(
        'Ivan Ivanov',
        'ivanov@qa.ru',
        'Male',
        '9850001122',
        '11 May,2001',
        'Arts, Biology',
        'Sports, Music',
        'photo.jpg',
        'Russia Moscow Red Square 1',
        'NCR Delhi'
    ))
