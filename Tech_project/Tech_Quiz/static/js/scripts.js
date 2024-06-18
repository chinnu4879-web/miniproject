document.addEventListener('DOMContentLoaded', function () {
    const questions = JSON.parse(document.getElementById('questions-data').textContent);
    const quizContainer = document.getElementById('quiz-container');

    questions.forEach(question => {
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');
        
        const questionTitle = document.createElement('h2');
        questionTitle.textContent = question.text;
        questionDiv.appendChild(questionTitle);
        
        question.options.forEach(option => {
            const optionLabel = document.createElement('label');
            const optionInput = document.createElement('input');
            optionInput.type = 'radio';
            optionInput.name = `question_${question.id}`;
            optionInput.value = option.id;
            optionLabel.appendChild(optionInput);
            optionLabel.appendChild(document.createTextNode(option.text));
            questionDiv.appendChild(optionLabel);
            questionDiv.appendChild(document.createElement('br'));
        });
        
        quizContainer.appendChild(questionDiv);
    });

    document.getElementById('submit-btn').addEventListener('click', function (e) {
        e.preventDefault();
        const resultsContainer = document.getElementById('results-container');
        resultsContainer.innerHTML = '';

        const formData = new FormData();
        questions.forEach(question => {
            const selectedOption = document.querySelector(`input[name="question_${question.id}"]:checked`);
            if (selectedOption) {
                formData.append(`question_${question.id}`, selectedOption.value);
            }
        });

        fetch('/submit_quiz/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            const scoreMessage = document.createElement('p');
            scoreMessage.textContent = `Your score: ${data.score}`;
            resultsContainer.appendChild(scoreMessage);

            if (data.score >= 30) {
                const passMessage = document.createElement('p');
                passMessage.classList.add('pass-message');
                passMessage.textContent = 'Congratulations! You passed the quiz.';
                resultsContainer.appendChild(passMessage);
            } else {
                const failMessage = document.createElement('p');
                failMessage.classList.add('fail-message');
                failMessage.textContent = 'Sorry, you failed the quiz. Try again.';
                resultsContainer.appendChild(failMessage);
            }
        });
    });
});