const searchBtn = document.getElementById("searchButton");

searchBtn.addEventListener('click', () => {
    const search = document.querySelector("#search");
    if(search.value){
        window.location.href = "/main/"+search.value;
    }else{
        alert("Please enter something to search...")       
    }
});

// Load Songs
function loadSong(lyrics_id, subtitle, id, enc_url, title, image){
    window.location.href = "/main/"+id+"/"+lyrics_id+"/?url="+enc_url+"&title="+title+"&subtitle="+subtitle+"&image="+image
}