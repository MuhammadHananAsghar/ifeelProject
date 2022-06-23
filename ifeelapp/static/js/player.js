/** Implementation of the functionality of the audio player */
const playBtn = document.getElementById("play-icon");
const volumeBtn = document.getElementById("volume-button");
const seekSlider = document.getElementById("seek-slider");
const volumeSlider = document.getElementById("volumeSlider");
const audio = document.querySelector("audio");
const durationContainer = document.getElementById("duration");
const currentTimeContainer = document.getElementById("current-time");

playBtn.onclick = () => {
  if (playBtn.className === "uil uil-play") {
    playBtn.className = "uil uil-pause";
  } else {
    playBtn.className = "uil uil-play";
  }
};

volumeBtn.onclick = () => {
  let vContainer = document.querySelector(".rangeContainer");
  if (vContainer.style.opacity === "" || vContainer.style.opacity === "0") {
    vContainer.style.opacity = "1";
  } else {
    vContainer.style.opacity = "0";
  }
};

// Calculating Time
const calculateTime = (secs) => {
  const minutes = Math.floor(secs / 60);
  const seconds = Math.floor(secs % 60);
  const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
  return `${minutes}:${returnedSeconds}`;
};

// Displaying Duration
const displayDuration = () => {
  const durationContainer = document.getElementById("duration");
  durationContainer.textContent = calculateTime(audio.duration);
};

// Setting Seek Slider max to
const setSliderMax = () => {
  seekSlider.max = Math.floor(audio.duration);
};

if (audio.readyState > 0) {
  // Get Buffered Audio
  let bufferedAmount = audio.buffered.end(audio.buffered.length - 1);
  // Get Playable Audio
  let seekableAmount = audio.seekable.end(audio.seekable.length - 1);

  displayDuration();
  setSliderMax();
} else {
  audio.addEventListener("loadedmetadata", () => {
    displayDuration();
    setSliderMax();
  });
}

// Playing Audio
playBtn.addEventListener("click", () => {
  if (playBtn.className === "uil uil-pause") {
    audio.play();
  } else {
    audio.pause();
  }
});

// Updating Time of Audio w.r.t seek
audio.addEventListener("timeupdate", () => {
  currentTimeContainer.textContent = calculateTime(seekSlider.value);
  seekSlider.value = Math.floor(audio.currentTime);
});

// Changing seekbar if user changes
seekSlider.addEventListener("change", () => {
  audio.currentTime = seekSlider.value;
});

seekSlider.oninput = () => {
  console.log(seekSlider.value);
};

// Volume Functionality implmenetation
volumeSlider.addEventListener("input", (e) => {
  const value = e.target.value;
  if(value == 1){
    volumeBtn.className = "uil uil-volume-mute";
  }else if(value < 50){
    volumeBtn.className = "uil uil-volume-down";
  }
  else{
    volumeBtn.className = "uil uil-volume-up";
  }
  audio.volume = value / 100;
});
