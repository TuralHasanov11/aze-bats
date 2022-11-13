function getCookie(name) {
  let cookieValue = null;

  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();

      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

        break;
      }
    }
  }

  return cookieValue;
}

const csrftoken = getCookie('csrftoken');
const loadBtn = document.querySelector('.load-bat-btn')
const galleryContainer = document.querySelector('.gallery-masonry')
const url = "load"
let page = 1

async function getBats() {
  await fetch(`${url}?page=${page}`, {
    credentials: 'include',
    method: 'GET',
    mode: 'same-origin',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
  })
    .then(res => res.json())
    .then(data => {
      setBats(data)
    })
    .catch(e => {
      console.log(e)
    })
}

let bats = [];

getBats()

loadBtn.addEventListener('click', (e) => {
  getBats()
})

function setBats(data) {
  let result = "";

  if (!data.pagination.has_next) {
    loadBtn.style.display = "none"
  }

  if (data.bats) {
    bats = bats.concat(data.bats)
    page++
    for (const bat of bats) {
      result += `<div class="category_1 col-sm-6 col-lg-4 col-xl-3 gallery-masonry__item">
          <a class="gallery-masonry__img gallery-masonry__item--height-1" href="${bat.cover_image}" data-fancybox="gallery">
            <img class="img--bg" src="${bat.cover_image}" alt="${bat.name}"/>
            <div class="gallery-masonry__description">
              <span>${bat.name}</span>
            </div>
          </a>
        </div>`
    }
  }

  galleryContainer.innerHTML = result
}