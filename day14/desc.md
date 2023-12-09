



Day 14 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#           [2015](/2015)

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.


Reindeer can only either be *flying* (always at their top speed) or *resting* (not moving at all), and always spend whole seconds in either state.


For example, suppose you have the following Reindeer:


* Comet can fly *14 km/s for 10 seconds*, but then must rest for *127 seconds*.
* Dancer can fly *16 km/s for 11 seconds*, but then must rest for *162 seconds*.


After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.


In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at *`1120`* km (poor Dancer has only gotten `1056` km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).


Given the descriptions of each reindeer (in your puzzle input), after exactly `2503` seconds, *what distance has the winning reindeer traveled*?



To begin, [get your puzzle input](14/input).


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Reindeer+Olympics%22+%2D+Day+14+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F14&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



