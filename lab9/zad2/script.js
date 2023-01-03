"use strict"
var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

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
  while (i < s.length && !isNaN(s.charAt(i)))
  {
      i++;
  }
  if (i > 0 && !isNaN(s.substring(0, i)))
      window.allSummed += parseInt(s.substring(0, i));
  return window.allSummed;
}

describe('The sum() function', function() {
 it('Returns 4 for 2+2', function() {
   expect(sum(2,2)).to.equal(4);
 });
 it('Returns 0 for -2+2', function() {
   expect(sum(-2,2)).to.equal(0);
 });
});

describe('The digitSum() function', function() {
  it('Returns 10 for 3a4b3c', function() {
    expect(digitSum('3a4b3c')).to.equal(10);
  });
  it('Returns 0 for abc', function() {
    expect(digitSum('abc')).to.equal(0);
  });
});

describe('The countLetters() function', function() {
  it('Returns 3 for 12ab3c', function() {
    expect(countLetters('12ab3c')).to.equal(3);
  });
  it('Returns 0 for 123', function() {
    expect(countLetters('123')).to.equal(0);
  });
});

describe('The totalSum() function', function() {
  mocha.setup({globals: ['allSummed']});
  it('Returns 123 for 123abc', function () {
    expect(totalSum('123')).to.equal(123);
  });
  it('Returns 110 for 100a and 10b12', function() {
    window.allSummed = 0;
    totalSum('100a');
    expect(totalSum('10b12')).to.equal(110);
  });
});