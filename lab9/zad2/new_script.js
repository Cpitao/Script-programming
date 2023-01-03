function digitSum(s) {
    var res = 0;
    for (var i=0; i < s.length; i++) {
      if (!isNaN(s.charAt(i)))
        res += parseInt(s.charAt(i));
    }
  
    return res;
}
  
function countLetters(s) {
    var count = 0;
    for (var i=0; i < s.length; i++) {
        if (s.charAt(i).toLowerCase() != s.charAt(i).toUpperCase()) count++;
    }

    return count;
}

function totalSum(s) {
    if (typeof(window.allSummed) === 'undefined') {
        window.allSummed = 0;
    }

    var i=0;
    while (!isNaN(s.charAt(i)) && i < s.length)
    {
        i++;
    }
    if (i > 0 && !isNaN(s.substring(0, i)))
        window.allSummed += parseInt(s.substring(0, i));
    return window.allSummed;
}

function prompter() {
    var s = window.prompt("Input:");
    if (s == null) return;
    var c = digitSum(s);
    var l = countLetters(s);
    var ts = totalSum(s);

    var p = document.createElement('p');
    p.innerHTML = "<p>" + s + "</p>" + "<span style='color:red'>" + "&emsp;" + c + "</span>" + "<span style='color:green'>";
    p.innerHTML += "&emsp;" + l + "</span>" + "<span style='color:blue'>" + "&emsp;" + ts + "</span>";
    document.body.appendChild(p);
    setTimeout(prompter, 0);
} 