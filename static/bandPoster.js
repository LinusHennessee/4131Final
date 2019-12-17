window.onload = function() {
        var tags = document.getElementsByTagName('td');
        for(var i = 0; i<tags.length; i++) {
            var tag = tags[i];
            tag.onclick = function() {
              var sibs = this.parentNode.children;
              parentRow = this.parentNode;
              document.getElementById("name").innerHTML = "Band Name: " + sibs[1].textContent;
              document.getElementById("singer").innerHTML = "Singer: " + sibs[4].textContent;
              document.getElementById("guitar").innerHTML = "Guitarist: " + sibs[5].textContent;
              document.getElementById("bass").innerHTML = "Bassist: " + sibs[6].textContent;
              document.getElementById("drummer").innerHTML = "Drummer: " + sibs[7].textContent;
              document.getElementById("poster").style.background = sibs[2].textContent;
              document.getElementById("poster").style.border = "7px solid " + sibs[3].textContent;

              document.getElementById("name").style.color = sibs[3].textContent;
              document.getElementById("singer").style.color = sibs[3].textContent;
              document.getElementById("guitar").style.color = sibs[3].textContent;
              document.getElementById("bass").style.color = sibs[3].textContent;
              document.getElementById("drummer").style.color = sibs[3].textContent;
            }
        }
    }
