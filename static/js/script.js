// Календарь в форме
flatpickr("#id_birthday", {
    dateFormat: "d.m.Y", // Формат даты
    locale: "ru", // Локализация
    allowInput: true // Разрешение ввода даты вручную
});

// Телефон в форме
let phoneInput = document.getElementById("id_phone");
let phoneMask = new Inputmask("+7 (999) 999-99-99");
phoneMask.mask(phoneInput);

// Скролл до формы
const firstButton = document.querySelector('.header_down-join-us')
const formBlock = document.querySelector('.fill-form')

firstButton.addEventListener('click', () => {
    formBlock.scrollIntoView({ behavior: 'smooth' })
})


// Плавное появление элементов при скролле
ScrollReveal().reveal('.scroll-reveal', { delay: 300 });

// Калькулятор; отправка данных
// const cityField = document.querySelector('.calc-city')
const vacancyField = document.querySelector('.calc-vacancy')
const cityFormField = document.querySelector('.fill-form-city')
const vacancyFormField = document.querySelector('.fill-form-vacancy')

const vacancyTitleText = document.querySelector('.earn-calc_description_name')
const salaryText = document.querySelector('.earn-calc_description_salary')
const responsibilitiesText = document.querySelector('.earn-calc_description_responsibilities_text')
const requirementsText = document.querySelector('.earn-calc_description_requirements_text')
const conditionsText = document.querySelector('.earn-calc_description_conditions_text')
const descriptionVacancyBlock = document.querySelector('.earn-calc_description')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let showInfo = (data) => {
    if (!data.city_is_not_selected) {
        let title = data.name
        vacancyTitleText.innerHTML = title
        let salary = data.salary
        salaryText.innerHTML = salary
        let responsibilities = data.responsibilities.replace(/\\\s/g, '').replace(/\\n/g, '<br/>')
        responsibilitiesText.innerHTML = responsibilities
        let requirements = data.requirements.replace(/\\\s/g, '').replace(/\\n/g, '<br/>')
        requirementsText.innerHTML = requirements
        let conditions = data.conditions.replace(/\\\s/g, '').replace(/\\n/g, '<br/>')
        conditionsText.innerHTML = conditions
    }

}

// const getVacancyData = (field) => {
//     city = cityField.options[cityField.selectedIndex].value
//     vacancy = vacancyField.options[vacancyField.selectedIndex].value

//     fetch('/calculator/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCookie('csrftoken')
//         },
//         body: JSON.stringify({
//             'city_id': city,
//             'vacancy_id': vacancy,
//             'field': field
//         })
//     })
//         .then(response => response.json())
//         .then(data => {
//             descriptionVacancyBlock.style.display = 'block'
//             if (data.status == 'not city') {
//                 // меняем город соответствующий вакансии
//                 let options = cityField.options
//                 let options_text = []
//                 for (var i = 0; i < options.length; i++) {
//                     options_text.push(options[i].textContent);
//                 }
//                 cityIndex = options_text.indexOf(data.city)
//                 cityField.selectedIndex = cityIndex

//                 // меняем список вакансий соответствующий городу
//                 let newOptions
//                 for (var i = 0; i < data.vacancies.length; i++) {
//                     newOptions += `<option value='${data.vacancies_ids[i]}'>${data.vacancies[i]}</option>`
//                 }
//                 vacancyField.innerHTML = newOptions
//                 let vacancyIndex = data.vacancies.indexOf(data.name)
//                 vacancyField.selectedIndex = vacancyIndex
//                 showInfo(data)
//             } else if (data.status == 'not vacancy') {
//                 let newOptions
//                 if (data.city_is_not_selected) {
//                     newOptions = `<option value>Выберите вакансию</option>`
//                     descriptionVacancyBlock.style.display = 'none'
//                 }

//                 let vacancies = data.vacancies
//                 for (let i = 0; i < vacancies.length; i++) {
//                     newOptions += `<option value='${data.vacancies_ids[i]}'>${vacancies[i]}</option>`
//                 }
//                 vacancyField.innerHTML = newOptions
//                 if (data.city_is_not_selected) {
//                     vacancyField.selectedIndex = 0;
//                 } else {
//                     let vacancyIndex = data.vacancies.indexOf(data.name)
//                     vacancyField.selectedIndex = vacancyIndex
//                 }

//                 showInfo(data)
//             }

//         })
// }

// cityField.addEventListener('change', () => {
//     getVacancyData('city')
// })

// vacancyField.addEventListener('change', () => {
//     getVacancyData('vacancy')
// })

const checkCityVacancy = (field) => {
    city = cityFormField.options[cityFormField.selectedIndex].value
    vacancy = vacancyFormField.options[vacancyFormField.selectedIndex].value

    fetch('/calculator/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'city_id': city,
            'vacancy_id': vacancy,
            'field': field
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == 'not city') {
                // меняем город соответствующий вакансии
                let options = cityField.options
                let options_text = []
                for (var i = 0; i < options.length; i++) {
                    options_text.push(options[i].textContent);
                }
                cityIndex = options_text.indexOf(data.city)
                cityFormField.selectedIndex = cityIndex

                // меняем список вакансий соответствующий городу
                let newOptions
                for (var i = 0; i < data.vacancies.length; i++) {
                    newOptions += `<option value='${data.vacancies_ids[i]}'>${data.vacancies[i]}</option>`
                }
                vacancyFormField.innerHTML = newOptions
                let vacancyIndex = data.vacancies.indexOf(data.name)
                vacancyFormField.selectedIndex = vacancyIndex
            } else if (data.status == 'not vacancy') {
                let newOptions
                let vacancies = data.vacancies
                for (let i = 0; i < vacancies.length; i++) {
                    newOptions += `<option value='${data.vacancies_ids[i]}'>${vacancies[i]}</option>`
                }
                vacancyFormField.innerHTML = newOptions
                let vacancyIndex = data.vacancies.indexOf(data.name)
                vacancyFormField.selectedIndex = vacancyIndex
            }

        })
}

// cityFormField.addEventListener('change', () => {
//     checkCityVacancy('city')
// })

// vacancyFormField.addEventListener('change', () => {
//     checkCityVacancy('vacancy')
// })

// гражданство
const citizenship = document.getElementById('id_citizenship')
const hiddenCitizenship = document.querySelector('.hidden')



const setToEndAnotherOption = () => {
    let options = citizenship.options
    let anotherIndex
    for (let i = 0; i < options.length; i++) {
        if (options[i].text == 'Другое') {
            anotherIndex = i
        }
    }
    let anotherOption = citizenship.options[anotherIndex]
    citizenship.appendChild(anotherOption)

}

citizenship.addEventListener('change', () => {
    let selectOption = citizenship.options[citizenship.selectedIndex].text

    if (selectOption == 'Другое') {
        hiddenCitizenship.style.display = 'block'
    } else {
        console.log()
        hiddenCitizenship.style.display = 'none'
    }
})

// radio кнопки
let radios = document.querySelectorAll('.fill-form-source')
let radioLabel_0 = document.getElementById('id_sources_0')
let radioLabel_1 = document.getElementById('id_sources_1')
let radioLabel_2 = document.getElementById('id_sources_2')
let radioLabel_3 = document.getElementById('id_sources_3')
let radioWrapper = document.querySelector('.fill-form-source-items')
// let radioLabels = radioWrapper.children

for(let i = 0; i < radios.length; i++) {
    radios[i].addEventListener('change', e => {
        let number = String(e.target.value - 1)
        for(let i = 0; i < radioLabels.length; i++) {
            let forAttr = radioLabels[i].htmlFor
            console.log(forAttr.includes(number))
            if(forAttr.includes(number)) {
                for(let i = 0; i < radioLabels.length; i++) {
                    radioLabels[i].classList.remove('fill-form-source-items_was_click')
                }
                radioLabels[i].classList.add('fill-form-source-items_was_click')
            }
        }
    })
}





document.addEventListener('DOMContentLoaded', () => {
    // checkCityVacancy('vacancy')
    setToEndAnotherOption()
})


// Slider

const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    slidesPerView: 2.7,
    spaceBetween: 30,
    loop: true,
    centeredSlides: true,
    speed: 1500,
    waitForTransition: true,
    simulateTouch:false,
    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 1.3,
        },
        400: {
            slidesPerView: 1.5,
        },
        545: {
            slidesPerView: 1.5,
        },
        800: {
            slidesPerView: 1.7,
        },
        // when window width is >= 480px
        900: {
            slidesPerView: 2.2,
        },
        // when window width is >= 640px
        1150: {
            slidesPerView: 3.7,
        }
    },
    autoplay: {
        delay: 100,
        disableOnInteraction: false,
    },



    // If we need pagination
    // pagination: {
    //   el: '.swiper-pagination',
    // },

    // // Navigation arrows
    // navigation: {
    //   nextEl: '.swiper-button-next',
    //   prevEl: '.swiper-button-prev',
    // },

    // // And if we need scrollbar
    // scrollbar: {
    //   el: '.swiper-scrollbar',
    // },
});

// вложение файла
const file = document.querySelector('.fill-form-file')
const fileIcon = document.querySelector('.file')

file.addEventListener('change', e => {
    const fileNameArr = e.target.files[0].name.split('.')
    const fileEx = fileNameArr[fileNameArr.length - 1]
    const fileExArr = ['doc', 'docx', 'pdf']
    fileExArr.includes(fileEx) 
    ? fileIcon.src = '/static/imgs/fileChange.png'
    : alert('Выберите файл в формате doc, docx или pdf')

})