try {
    let elements = document.querySelectorAll('.step');
    let currentIndex = 0;
    let showPreviousButton = document.querySelector('#return');
    let back = document.querySelector('#back');
    let showNextButton = document.querySelector('#next');
    let submitButton = document.querySelector('#submit_q');
    let h1 = document.querySelector('#h1');

    function showPrevious() {
        elements[currentIndex].classList.remove('visible2');
        h1.innerHTML = `<b>Шаг ${currentIndex}</b>`
        currentIndex = (currentIndex - 1 + elements.length) % elements.length;
        elements[currentIndex].classList.add('visible2');
        updateButtonVisibility();
    }

    function showNext() {
        if(validateInputs()===false){
            alert('Пожалуйста, заполните все обязательные поля.');
            return false
        }
        elements[currentIndex].classList.remove('visible2');
        h1.innerHTML = `<b>Шаг ${currentIndex}</b>`
        currentIndex = (currentIndex + 1) % elements.length;
        elements[currentIndex].classList.add('visible2');
        updateButtonVisibility();
    }

    function updateButtonVisibility() {
        back.style.display = currentIndex === 0 ? 'block' : 'none';
        showPreviousButton.style.display = currentIndex === 0 ? 'none' : 'block';
        h1.innerHTML = `<b>Шаг ${currentIndex + 1}</b>`
        showNextButton.style.display = currentIndex === elements.length - 1 ? 'none' : 'block';
        submitButton.style.display = currentIndex === elements.length - 1 ? 'block' : 'none';
    }
    function back2() {
        window.history.back();
    }
    function validateInputs() {
        let currentStep = elements[currentIndex];
        if (currentStep) {
            let inputs = currentStep.querySelectorAll('input[required], select[required], textarea[required]');
            for (let input of inputs) {
                if (!input.value.trim()) {
                    return false;
                }
            }
            return true;
        }
        
    }

    elements[currentIndex].classList.add('visible2');
    updateButtonVisibility();
}
catch {
    console.log('Не та страница');
}


