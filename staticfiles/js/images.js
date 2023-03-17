const thumbnails = document.querySelectorAll('.thumbnail');
const mainPhoto = document.querySelector('.main-photo');

thumbnails.forEach((thumbnail) => {
  thumbnail.addEventListener('click', () => {
    // удаляем класс "active" у всех маленьких фотографий
    thumbnails.forEach((t) => t.classList.remove('active'));

    // добавляем класс "active" к текущей маленькой фотографии
    thumbnail.classList.add('active');

    // меняем источник большой фотографии на текущую маленькую
    mainPhoto.classList.add('fade-in'); // добавляем класс для анимации
    mainPhoto.addEventListener('animationend', () => {
      // удаляем класс для анимации после ее окончания
      mainPhoto.classList.remove('fade-in');
    });
    mainPhoto.src = thumbnail.src;
  });
});