$(document).ready(function(){	
    var crunch1 = document.createElement('audio');
    crunch1.setAttribute('src', 'assets/crunch1.mp3');
    var crunch2 = document.createElement('audio');
    crunch2.setAttribute('src', 'assets/crunch2.mp3');
    var crunch3 = document.createElement('audio');
    crunch3.setAttribute('src', 'assets/crunch3.mp3');
    
	function whichAnimationEvent(){
	  var t,
	      el = document.createElement("fakeelement");

	  var animations = {
	    "animation"      : "animationend",
	    "OAnimation"     : "oAnimationEnd",
	    "MozAnimation"   : "animationend",
	    "WebkitAnimation": "webkitAnimationEnd"
	  }

	  for (t in animations){
	    if (el.style[t] !== undefined){
	      return animations[t];
	    }
	  }
	}

	var animationEvent = whichAnimationEvent();
	var breakSteps = ['break1', 'break2', 'break3']
	var ind = 0
	$('body').click(function(){
		if(ind < breakSteps.length){
			switch(breakSteps[ind]){
				case 'break1':
					crunch1.play();
					$('#cookie').attr('src', "assets/cookiecrack1.png")
					$('#cookie').addClass('break1')
					break;
				case 'break2':
					crunch2.play();
					$('#cookie').attr('src', "assets/cookiecrack2.png")
					$('#cookie').removeClass('break1')
					$('#cookie').addClass('break2')
					break;
				case 'break3':
					crunch3.play();
					$('#cookie').attr('style', 'display: none')
					$('#chalfL').attr('style', 'display: block')
					$('#chalfL').addClass('break3L')
					$('#chalfR').attr('style', 'display: block')
					$('#chalfR').addClass('break3R')
					$('#chalfL').one(animationEvent, function(event){
						$('#chalfL').attr('style', 'display: none')
						$('#paper').attr('style', 'display: flex')
						$('#paper').addClass('fadein')
					});
					$('#chalfR').one(animationEvent, function(event){
						$('#chalfR').attr('style', 'display: none')
					});					
					break;
			}
			ind++;
		}
	})
})