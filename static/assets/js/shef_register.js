document.getElementById('next').addEventListener('click', function() {
    var currentStep = document.querySelector('.step:not(.d-none)');
    var nextStep = currentStep.nextElementSibling;

    if (nextStep && nextStep.id.startsWith('step_')) {
        currentStep.classList.add('d-none');
        nextStep.classList.remove('d-none');
    }
});

document.getElementById('return').addEventListener('click', function() {
    var currentStep = document.querySelector('.step:not(.d-none)');
    var prevStep = currentStep.previousElementSibling;

    if (prevStep && prevStep.id.startsWith('step_')) {
        currentStep.classList.add('d-none');
        prevStep.classList.remove('d-none');
    }
});