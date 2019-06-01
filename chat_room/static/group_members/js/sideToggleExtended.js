(function($){
  $.fn.sideToggle = function(options) {


    var settings = $.extend({
      moving : null, // which object to toggle?
      direction : null, // toggle from this side of the window
        opacity: 1,
    }, options);


    return this.click(function(){

      var thisDir = {};

      var moveThis = settings.moving;
      var dirPos = parseInt($(moveThis).css(settings.direction), 10);
      var menuWidth = $(moveThis).outerWidth();

      if (isNaN(dirPos)) {
        console.log("Please define the object's position in the css.");
      }

      if (dirPos === 45) {
        thisDir[settings.direction] = 0;
        thisDir[settings.opacity] = 0;
        $(moveThis).animate(thisDir);
      } else {
        thisDir[settings.direction] = 45;
        thisDir[settings.opacity] = 1;
        $(moveThis).animate(thisDir);
      }
    });
  }
}(jQuery));

