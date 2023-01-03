function formSubmitted() {
    const fields = document.forms[0];
    var p = document.createElement('p');

    p.innerHTML = (typeof(fields.elements.pole_tekstowe.value) + ' ' + fields.elements.pole_tekstowe.value);
    p.innerHTML += '\n' + (typeof(fields.elements.pole_liczbowe.value) + ' ' + fields.elements.pole_liczbowe.value);
    document.body.appendChild(p);
}

function onloadFunc() {
    console.log('Tekst 1');
    window.alert('Tekst 2');
}
console.log(window.prompt("Tekst1","Tekst2")); 
// Text above input and default value of input
// if clicked OK then string with input value else null (object)