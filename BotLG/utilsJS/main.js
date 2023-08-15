const divsHidden = document.getElementsByClassName("day-timeline-list-wrap collapse")

for(let i = 0; i<divsHidden.length; i++){
    try {
        divsHidden[i].classList.remove("collapse")
        divsHidden[i].classList.add("show")
    } catch (error) {
    
    }
    
}