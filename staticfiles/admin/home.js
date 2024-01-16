<script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>

  document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
      slidesPerView: 1,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  });



  function toggleModal() {
    var modal = document.getElementById("userModal");
    modal.style.display = modal.style.display === "block" ? "none" : "block";
  }


  function displayCVModal() {
  var modal = document.getElementById("cvModal");
  modal.style.display = "block";
  generateCVCards();
}

function generateCVCards() {
  var cvData = [
    { user: "John Doe", cv: "CV1.pdf", email: "john@example.com", phone: "1234567890" },
    { user: "Jane Smith", cv: "CV2.pdf", email: "jane@example.com", phone: "9876543210" },
    // Add more CV data as needed
  ];

  var cvCardsContainer = document.querySelector(".cv-cards-container");
  cvCardsContainer.innerHTML = ""; // Clear the container

  cvData.forEach(function(cv) {
    var card = document.createElement("div");
    card.classList.add("cv-card");
    card.innerHTML = `
      <h3>${cv.user}</h3>
      <p>Email: ${cv.email}</p>
      <p>Phone: ${cv.phone}</p>
      <button onclick="viewCV('${cv.cv}')">View CV</button>
      <button onclick="deleteCV('${cv.cv}')">Delete</button>
    `;
    cvCardsContainer.appendChild(card);
  });
}

function deleteCV(cv) {
  // Implement CV deletion logic here
}

function viewCV(cvUrl) {
  // Open a new tab/window to view the CV
  window.open(cvUrl);
}

function closeCVModal() {
  var modal = document.getElementById("cvModal");
  modal.style.display = "none";
}





  function toggleForm(formId) {
    var form = document.getElementById(formId);
    form.classList.toggle("hidden");
  }


<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>

  function displayAnalyticsModal() {
    var modal = document.getElementById("analyticsModal");
    modal.style.display = "block";
    generateAnalyticsChart();
  }

  function closeAnalyticsModal() {
    var modal = document.getElementById("analyticsModal");
    modal.style.display = "none";
  }

  function generateAnalyticsChart() {
    
    var options = {
      series: [{
        name: 'Sales',
        type: 'column',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
      }, {
        name: 'Profit',
        type: 'line',
        data: [20, 35, 40, 60, 60, 75, 80, 90, 100]
      }],
      chart: {
        height: 350,
        type: 'line',
      background: '#222',
      },
      stroke: {
        width: [0, 4]
      },
      title: {
        text: 'Sales & Profit'
      },
      dataLabels: {
        enabled: true,
        enabledOnSeries: [1]
      },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
      }
    };

    var chart = new ApexCharts(document.querySelector("#chartContainer"), options);
    chart.render();
  }



  function toggleLogin() {
    var loginModal = document.getElementById("loginModal");
    var overlay = document.getElementById("overlay");
    loginModal.style.display = "block";
    overlay.style.display = "block";
  }

  function closeLogin() {
    var loginModal = document.getElementById("loginModal");
    var overlay = document.getElementById("overlay");
    loginModal.style.display = "none";
    overlay.style.display = "none";
  }

  function stopPropagation(event) {
    event.stopPropagation();
  }
