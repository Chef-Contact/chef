// let steps = document.querySelectorAll('.step');
// let currentStepIndex = 0;
// function extractAndConcatenateNumbersFromString(str) {
//     let regex = /\d+(\.\d+)?/g;
//     let numbers = str.match(regex);

//     if (numbers !== null) {
//         let concatenatedNumbers = numbers.join('');
//         return Number(concatenatedNumbers);
//     } else {
//         return '';
//     }
// }
// let lastIndex = extractAndConcatenateNumbersFromString(steps[steps.length - 1].id);

// showStep(currentStepIndex);

// function showStep(index) {
//     for (let i = 0; i < steps.length; i++) {
//         if (i === index) {
//             steps[i].classList.remove('d-none');
//         }else{
//             steps[i].classList.add('d-none');
//         }
//     }
//     document.getElementById('return').classList.toggle('d-none', index === 0);
//     document.getElementById('next').setAttribute('type', (index == lastIndex) ? 'submit' : 'button');
//     document.getElementById('next').setAttribute('textContent', (index == lastIndex) ? 'Aproove' : 'Next');
// }

// document.getElementById('next').addEventListener('click', function() {
//     currentStepIndex++;
//     if (currentStepIndex >= steps.length) {
//         currentStepIndex = steps.length - 1;
//     }
//     console.log(currentStepIndex);
//     showStep(currentStepIndex);
// });

// document.getElementById('return').addEventListener('click', function() {
//     currentStepIndex--;
//     if (currentStepIndex < 0) {
//         currentStepIndex = 0;
//     }
//     showStep(currentStepIndex);
// });

let elements = document.querySelectorAll('.step');
let currentIndex = 0;
let showPreviousButton = document.querySelector('#return');
let showNextButton = document.querySelector('#next');
let submitButton = document.querySelector('#submit_q');
const quiz__error = document.querySelector('.quiz__error')
const ok_btn = document.querySelector('#ok_btn')

function showPrevious() {
    elements[currentIndex].classList.remove('visible2');
    currentIndex = (currentIndex - 1 + elements.length) % elements.length;
    elements[currentIndex].classList.add('visible2');
    updateButtonVisibility();
}

function showNext() {
    elements[currentIndex].classList.remove('visible2');
    currentIndex = (currentIndex + 1) % elements.length;
    elements[currentIndex].classList.add('visible2');
    updateButtonVisibility();
}

function updateButtonVisibility() {
    showPreviousButton.style.display = currentIndex === 0 ? 'none' : 'block';
    showNextButton.style.display = currentIndex === elements.length - 1 ? 'none' : 'block';
    submitButton.style.display = currentIndex === elements.length - 1 ? 'block' : 'none';
}

elements[currentIndex].classList.add('visible2');
updateButtonVisibility();
