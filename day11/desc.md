



Day 11 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#    0xffff&[2015](/2015)

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.


To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by *incrementing* his old password string repeatedly until it is valid.


Incrementing is just like counting with numbers: `xx`, `xy`, `xz`, `ya`, `yb`, and so on. Increase the rightmost letter one step; if it was `z`, it wraps around to `a`, and repeat with the next letter to the left until one doesn't wrap around.


Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:


* Passwords must include one increasing straight of at least three letters, like `abc`, `bcd`, `cde`, and so on, up to `xyz`. They cannot skip letters; `abd` doesn't count.
* Passwords may not contain the letters `i`, `o`, or `l`, as these letters can be mistaken for other characters and are therefore confusing.
* Passwords must contain at least two different, non-overlapping pairs of letters, like `aa`, `bb`, or `zz`.


For example:


* `hijklmmn` meets the first requirement (because it contains the straight `hij`) but fails the second requirement requirement (because it contains `i` and `l`).
* `abbceffg` meets the third requirement (because it repeats `bb` and `ff`) but fails the first requirement.
* `abbcegjk` fails the third requirement, because it only has one double letter (`bb`).
* The next password after `abcdefgh` is `abcdffaa`.
* The next password after `ghijklmn` is `ghjaabcc`, because you eventually skip all the passwords that start with `ghi...`, since `i` is not allowed.


Given Santa's current password (your puzzle input), what should his *next password* be?



Your puzzle input is `hepxcrrq`.


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Corporate+Policy%22+%2D+Day+11+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F11&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



