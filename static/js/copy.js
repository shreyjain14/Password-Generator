function copyPassword() {
      var copyText = document.getElementById("password");
      copyText.select();
      copyText.setSelectionRange(0, 99999);
      navigator.clipboard.writeText(copyText.value);

      var tooltip = document.getElementById("myTooltip");
      tooltip.innerHTML = "Copied to Clipboard";
}

alert('test')