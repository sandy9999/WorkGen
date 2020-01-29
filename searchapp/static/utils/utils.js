const base64ToArrayBuffer = (base64) => {
    let binaryString = window.atob(base64.replace(/\s/g, ''));
    let binaryLen = binaryString.length;
    let bytes = new Uint8Array(binaryLen);
    for (let i = 0; i < binaryLen; i++) {
       let ascii = binaryString.charCodeAt(i);
       bytes[i] = ascii;
    }
    return bytes;
  };

const saveByteArray = (reportName, byte, type) => {
    let blob = new Blob([byte], {type: type});
    saveAs(blob, reportName);
  };

export {base64ToArrayBuffer, saveByteArray};
