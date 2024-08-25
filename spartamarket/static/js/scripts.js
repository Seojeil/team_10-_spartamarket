function HachTagInput(event) {
    const input = event.target;
    const invalidChar = /[^a-zA-Z0-9,가-힣\u3131-\u3163]/g;
    input.value = input.value.replace(invalidChar, '');
}