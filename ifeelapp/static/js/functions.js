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
function loadSong(lyrics_id, subtitle, id, enc_url, title, image, csrf_token){
    var data = {
        "lyrics_id": lyrics_id,
        "subtitle": subtitle,
        "id": id,
        "enc_url": enc_url,
        "title": title,
        "image": image
    };

        $.ajax({
        type: "POST",
        url: '/main/song/',
        data: { csrfmiddlewaretoken: csrf_token, data: data },
        success: function callback(response){
                    console.log(response);
        }
    });
    // window.location.href = "/main/"+id+"/"+lyrics_id+"/?url="+enc_url+"&title="+title+"&subtitle="+subtitle+"&image="+image
}