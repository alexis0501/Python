const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello tyler's  world is the best     ";
const expected2 = "hello tyler's  world is the best";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str){
    let trimmedStr = ' ';
    let firstChar = 0;
    let lastChar = str.length - 1;

    while(str[firstChar] === ' ')
        firstChar++;

    while(str[lastChar] === ' ')
        lastChar--;

    for(var x = firstChar; x< lastChar + 1; x++)
        trimmedStr += str[x];
    
    return trimmedStr
}

console.log(trim(str1))



const two_strA1 = "yes";
const two_strB1 = "eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;


    