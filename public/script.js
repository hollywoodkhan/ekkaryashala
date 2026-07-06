document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('learnBtn');
  const today = document.getElementById('today');

  if (button) {
    button.addEventListener('click', () => {
      alert('You are exploring a simple static website. Great start!');
    });
  }

  if (today) {
    const now = new Date();
    today.textContent = 'Today: ' + now.toDateString();
  }
});
