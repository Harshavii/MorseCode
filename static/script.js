function displayInput(event) {
    event.preventDefault();
    const inputElement = document.getElementById('textInput');
    const inputValue = inputElement.value;

    const outputElement = document.getElementById('output');
    outputElement.innerText = output;

    if (inputValue.trim() === '') {
        outputElement.style.display = 'none';
    } else {
        outputElement.style.display = 'block';
    }

    inputElement.value = '';
    return false;
}
