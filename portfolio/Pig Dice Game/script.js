'use strict';

///////////////////////////////////////
// Modal window

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.btn--close-modal');
const btnsOpenModal = document.querySelectorAll('.btn--show-modal');

const openModal = function (e) {
  e.preventDefault();
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

btnsOpenModal.forEach(btn => btn.addEventListener('click', openModal));

btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});

///section 186  - how to select, create, and delete elements
///selecting elements
console.log(document.documentElement); //selects the entire document
console.log(document.head); //selects head
console.log(document.body); //selects body

const header = document.querySelector('.header');
const allSelections = document.querySelectorAll('.section');
console.log(allSelections); // returns a list of nodes

document.getElementById('section--1');
document.getElementsByTagName('button'); //returns an HTML collection
document.getElementsByClassName('btn'); //returns an HTML collection

//creating and inserting elements
//.insertAdjacentHTML

const message = document.createElement('div'); //creating an object by class name div that represents a dom elememt
message.classList.add('cookie-message'); //adding the class
message.textContent =
  'We use cookies for improved functionality and analytics.';
message.innerHTML =
  'We use cookies for improved functionality and analytics. <button class="btn btn--close-cookie">got it!</button>';

//header.prepend(message);
header.append(message);
//header.append(message.cloneNode(true));
//header.before(message);
//header.after(message);

//make the got it button work:
document
  .querySelector('.btn--close-cookie')
  .addEventListener('click', function () {
    message.remove();
  });

//styles
message.style.backgroundColor = '#37383d';
message.style.width = '120%';

//retrieving style
//if we set it in JS - it's called "inline"
console.log(message.style.backgroundColor);
//if it's not - say it's computed
console.log(getComputedStyle(message).color);
