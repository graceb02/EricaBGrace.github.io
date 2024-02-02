'use strict';

//define the secret number with the random number generator (btw 1 and 20)
let secretNumber = Math.trunc(Math.random() * 20) + 1;
//document.querySelector('.number').textContent = secretNumber;
//define the score and high score
let score = 20;
let highscore = 0;

//making a function for setting the message
const displayMessage = function (message) {
  document.querySelector('.message').textContent = message;
};

//event listener for clicking the check button
//after the check button is clicked, it takes what we type into the box as our guess and puts it into the guess variable and then saves it to a variable guess.
document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);

  // when no number was entered
  if (!guess) {
    displayMessage('⛔️ No number!');

    //when guess is right and player wins
  } else if (guess === secretNumber) {
    displayMessage('🎉 Correct Number!');
    document.querySelector('.number').textContent = secretNumber;
    document.querySelector('body').style.backgroundColor = '#60b347'; //background color changes
    document.querySelector('.number').style.width = '30rem'; //making box wider
    if (score > highscore) {
      //setting highscore
      highscore = score;
      document.querySelector('.highscore').textContent = highscore;
    }
    //when guess is wrong
  } else if (guess !== secretNumber) {
    if (score > 1) {
      displayMessage(guess > secretNumber ? '📈 Too High!' : '📉 Too Low!');
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      //when no more guesses available
      displayMessage('💥 You lost the game!');
      document.querySelector('.score').textContent = 0;
    }
  }
});
// play again - reset score, pick new secret number, etc
document.querySelector('.again').addEventListener('click', function () {
  score = 20;
  secretNumber = Math.trunc(Math.random() * 20) + 1;
  displayMessage('Start guessing...');
  document.querySelector('.score').textContent = score;
  document.querySelector('.number').textContent = '?';
  document.querySelector('.guess').value = '';
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
});
