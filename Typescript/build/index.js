var dir;
(function (dir) {
    dir[dir["x"] = 1] = "x";
    dir[dir["y"] = 123] = "y";
    dir[dir["z"] = '123123'.length] = "z";
})(dir || (dir = {}));
console.log(dir)
var d = [dir.x, dir.y, dir.z];
console.log(d);
