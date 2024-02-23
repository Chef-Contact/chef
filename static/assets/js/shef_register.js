try{
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
}
catch{
    console.log('Не та страница');
}


