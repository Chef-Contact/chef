let steps = document.querySelectorAll('.step');
let currentStepIndex = 0;
showStep(currentStepIndex);

function showStep(index) {
    for (let i = 0; i < steps.length; i++) {
        if (i === index) {
            steps[i].classList.remove('d-none');
        }else{
            steps[i].classList.add('d-none');
        }
    }
    document.getElementById('return').classList.toggle('d-none', index === 0);
    document.getElementById('next').textContent = (index === 11 ) ? 'Finish' : 'Next';
    document.getElementById('next').type = (index === 11 ) ? 'submit' : 'button';
}

document.getElementById('next').addEventListener('click', function() {
    currentStepIndex++;
    if (currentStepIndex >= steps.length) {
        currentStepIndex = steps.length - 1;
    }
    showStep(currentStepIndex);
});

document.getElementById('return').addEventListener('click', function() {
    currentStepIndex--;
    if (currentStepIndex < 0) {
        currentStepIndex = 0;
    }
    showStep(currentStepIndex);
});