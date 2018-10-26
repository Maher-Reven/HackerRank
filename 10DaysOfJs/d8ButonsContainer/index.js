const centerBtn = document.querySelector('#btn5');
let outerGridItems = ['1', '2', '3', '6', '9', '8', '7', '4'];

const btn1 = document.querySelector('#btn1');
const btn2 = document.querySelector('#btn2');
const btn3 = document.querySelector('#btn3');
const btn6 = document.querySelector('#btn6');
const btn9 = document.querySelector('#btn9');
const btn8 = document.querySelector('#btn8');
const btn7 = document.querySelector('#btn7');
const btn4 = document.querySelector('#btn4');

const rotateText = () => {
  let popped = outerGridItems.pop();
  outerGridItems.unshift(popped);
  btn1.innerHTML = outerGridItems[0];
  btn2.innerHTML = outerGridItems[1];
  btn3.innerHTML = outerGridItems[2];
  btn6.innerHTML = outerGridItems[3];
  btn9.innerHTML = outerGridItems[4];
  btn8.innerHTML = outerGridItems[5];
  btn7.innerHTML = outerGridItems[6];
  btn4.innerHTML = outerGridItems[7];
};

centerBtn.addEventListener('click', rotateText);