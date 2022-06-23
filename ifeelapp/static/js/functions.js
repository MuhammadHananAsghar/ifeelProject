const searchBtn = document.getElementById("searchButton");

searchBtn.addEventListener("click", () => {
  const search = document.querySelector("#search");
  if (search.value) {
    window.location.href = "/main/" + search.value;
  } else {
    alert("Please enter something to search...");
  }
});

// Migration Functions
function migrate(address){
    window.location.href = "/main/"+address;
}

// Load Songs
function loadSong(lyrics_id, subtitle, id, enc_url, title, image, csrf_token) {
  var data = {
    lyrics_id: lyrics_id,
    subtitle: subtitle,
    id: id,
    enc_url: enc_url,
    title: title,
    image: image,
  };

  $.ajax({
    type: "POST",
    url: "/main/song/",
    data: { csrfmiddlewaretoken: csrf_token, data: data },
    success: function callback(response) {
      const audio = document.querySelector("audio");
      const image = document.getElementById("songImage");
      const title = document.getElementById("songTitle");
      const subtitle = document.getElementById("songDesc");

      localStorage.setItem("songurl", response["songurl"]);
      localStorage.setItem("image", response["image"]);
      localStorage.setItem("title", response["title"]);
      localStorage.setItem("subtitle", response["subtitle"]);
      audio.src = response["songurl"];
      image.src = response["image"];
      title.textContent = response["title"];
      subtitle.textContent = response["subtitle"];
    },
  });
}

if (localStorage.getItem("songurl")) {
  const audio = document.querySelector("audio");
  const image = document.getElementById("songImage");
  const title = document.getElementById("songTitle");
  const subtitle = document.getElementById("songDesc");

  audio.src = localStorage.getItem("songurl");
  image.src = localStorage.getItem("image");
  title.textContent = localStorage.getItem("title");
  subtitle.textContent = localStorage.getItem("subtitle");
}
// Downloader Function
function downloadFileWithLink(href) {
  var link = document.createElement("a");
  let name = (href?.split("/") || [])
  name = name[name?.length-1]
  link.setAttribute('download', name);
  link.href = href;
  document.body.appendChild(link);
  link.click();
  link.remove();
}

// Download
function download(id, url, csrf_token){
  var data = {
    id: id,
    enc_url: url
  };

  $.ajax({
    type: "POST",
    url: "/main/download/",
    data: { csrfmiddlewaretoken: csrf_token, data: data },
    success: function callback(response) {
      downloadFileWithLink(response['songurl']);
    },
  });
}