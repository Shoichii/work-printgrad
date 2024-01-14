window.addEventListener('DOMContentLoaded', () => {
    let startTime = document.querySelectorAll('.field-start_date_display')
    let tableString1 = document.querySelectorAll('.even')
    let tableString2 = document.querySelectorAll('.odd')
    let tableString = [...tableString1, ...tableString2]
    // setInterval(() => checkSLA(startTime,tableString), 100)
    checkSLA(startTime,tableString)
})

function transformDate(string) {
    let dateArray = string.split(/[\s.:]/);
    let day = dateArray[2];
    let month = dateArray[3] - 1;
    let year = dateArray[4];
    let hour = dateArray[0];
    let minute = dateArray[1];
    let date = new Date(year, month, day, hour, minute);
    return date
}

function checkSLA(startTime,tableString) {
    let dateNow = new Date()
    for (let i = 0; i < tableString.length; i++) {
        let startTime = tableString[i].children[2]
        let time = startTime.firstElementChild.firstElementChild.innerHTML
        let date2 = transformDate(time)
        let milliseconds = dateNow - date2
        let hours = milliseconds / 3600000;
        let status = tableString[i].children[1].firstElementChild.innerHTML
        if (hours >= 3 && status == 'Назначен') {
            tableString[i].style.backgroundColor = 'rgba(252, 158, 12, 0.5)'
        }
    }
}