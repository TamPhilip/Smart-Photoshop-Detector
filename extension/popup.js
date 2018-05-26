let addBorder = document.getElementById('addBorder');

addBorder.onclick = function(element){
    chrome.tabs.query({ active : true,  currentWindow : true}, function(tabs){
        chrome.tabs.executeScript(
            tabs[0].id,
            {file: 'createBorder.js'});
    });
}
