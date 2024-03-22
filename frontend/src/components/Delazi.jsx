import { useState, useRef } from "react";
import { MdLockOutline, MdLockOpen } from "react-icons/md";
import Subpage from "./Subpage";
import TextInput from "./TextInput";
import FileInput from "./FileInput";
import FileOutput from "./FileOutput";
import { stringToHex, hexToString } from "../helpers";

const Delazi = () => {
  const [format, setFormat] = useState("text");
  const [fileInputName, setFileInputName] = useState("");
  const [fileOutputName, setFileOutputName] = useState("");
  const [fileInput, setFileInput] = useState(null);
  const [fileURL, setFileURL] = useState(null);
  const [userInput, setUserInput] = useState("");
  const [userOutput, setUserOutput] = useState("");
  const outputTextArea = useRef(null);

  const [encryptionMode, setEncryptionMode] = useState("ecb");
  const [cfbBitSize, setCfbBitSize] = useState("2");
  const [ofbBitSize, setOfbBitSize] = useState("2");

  const [key, setKey] = useState("");
  const [mode, setMode] = useState("ecb");
  const [round, setRound] = useState(16);
  const [size, setSize] = useState(2);

  const handleFormat = (format) => {
    setFormat(format);
  };

  const handleUserInput = (textInput) => {
    setUserInput(textInput);
  };
  const handleFileInputChange = (event) => {
    const file = event.target.files[0];
    setFileInputName(file.name);
    setFileInput(file);

    const reader = new FileReader();
    reader.onload = (e) => {
      setUserInput(e.target.result);
    };
    reader.readAsDataURL(file);
  };

  const handleFileOutputChange = (fileNameInput) => {
    setFileOutputName(fileNameInput);
  };

  const encryptAction = async () => {
    if (format === "text") {
      await delaziEncryptAction();
    } else {
      await delaziFileEncryptMessage();
    }
  };

  const delaziEncryptAction = async () => {
    try {
      const response = await fetch("http://localhost:8080/delazi_encrypt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          plaintext: userInput,
          key: key,
          round: round,
          mode: mode,
          size: size,
        }),
      });
      const data = await response.json();
      if (data.status != 200) {
        setUserOutput("Error encrypting message.");
        return;
      }
      const encrypted = hexToString(data.message.encrypted);
      setUserOutput(encrypted);
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error encrypting message.");
    }
  };

  const delaziFileEncryptMessage = async () => {
    try {
      const formData = new FormData();
      formData.append("file", fileInput);
      formData.append("key", key);

      const response = await fetch(
        "http://localhost:8080/delazi_file_encrypt",
        {
          method: "POST",
          body: formData,
        }
      );

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      setFileURL(url);

      const reader = new FileReader();
      reader.onload = function (event) {
        setUserOutput(event.target.result);
      };

      reader.readAsText(blob, "ASCII");
    } catch (error) {
      console.error("Error:", error);
      setUserOutput("Error downloading file.");
    }
  };

  const decryptAction = async () => {
    if (format === "text") {
      await delaziDecryptAction();
    } else {
      await delaziFileDecryptMessage();
    }
  };

  const delaziDecryptAction = async () => {
    try {
      const response = await fetch("http://localhost:8080/delazi_decrypt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ciphertext: userInput,
          key: key,
          round: round,
          mode: mode,
          size: size,
        }),
      });

      const data = await response.json();
      if (data.status != 200) {
        setUserOutput("Error encrypting message.");
        return;
      }
      const decrypted = hexToString(data.message.decrypted);
      setUserOutput(decrypted);
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error encrypting message.");
    }
  };

  const delaziFileDecryptMessage = async () => {
    try {
      const formData = new FormData();
      formData.append("file", fileInput);
      formData.append("key", key);

      const response = await fetch(
        "http://localhost:8080/delazi_file_decrypt",
        {
          method: "POST",
          body: formData,
        }
      );

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      setFileURL(url);

      const reader = new FileReader();
      reader.onload = function (event) {
        setUserOutput(event.target.result);
      };

      reader.readAsText(blob, "ASCII");
    } catch (error) {
      console.error("Error:", error);
      setUserOutput("Error downloading file.");
    }
  };

  const handleFileOutputSubmit = () => {
    const element = document.createElement("a");
    const file = new Blob([outputTextArea.current.value], {
      type: "text/plain",
    });

    if (format === "file") {
      element.href = fileURL;
    } else {
      element.href = URL.createObjectURL(file);
    }

    element.download = fileOutputName ? fileOutputName : "encrypted";
    document.body.appendChild(element); // Firefox
    element.click();
  };

  return (
    <>
      <div className="p-2 bg-primary_1 rounded-md">
        {/* format picker */}
        <Subpage
          currentVariable={format}
          handleVariable={handleFormat}
          variables={["text", "file"]}
        />

        {/* input/output */}
        <div className="flex">
          {/* input */}
          <div className="basis-5/12 flex-col mx-1">
            <h2 className="h-8 items-center ml-1 mb-2 flex text-lg font-semibold text-white">
              Input
            </h2>
            {/* text input */}
            {format === "text" && (
              <TextInput handleOnChangeParent={handleUserInput} />
            )}

            {/* file input */}
            {format === "file" && (
              <FileInput
                handleOnChangeParent={handleFileInputChange}
                fileName={fileInputName}
              />
            )}
          </div>

          {/* key */}
          <div className="basis-2/12 flex-col mx-1">
            {/* Select Mode */}
            <h2 className="h-8 items-center mb-4 flex text-lg font-semibold text-white">Select Mode:</h2>
            <select
              value={encryptionMode}
              onChange={(e) => setEncryptionMode(e.target.value)}
              className="border rounded-md p-2 bg-primary_2 rounded-md border border-primary_3 text-white-800 focus:outline-none focus:ring-2 focus:ring-blue-50"
            >
              <option value="ecb" >ECB</option>
              <option value="cbc">CBC</option>
              <option value="cfb">CFB</option>
              <option value="ofb">OFB</option>
              <option value="ctr">CTR</option>
            </select>

            {encryptionMode === "cfb" && (
              <div className="mt-3">
                <h3 className="h-8 items-center ml-1 mt-3 flex text-lg font-semibold text-white">Select CFB Bit Size:</h3>
                <div className="flex items-center space-x-4">
                  <label className="flex items-center">
                    <input
                      type="radio"
                      value="2"
                      checked={cfbBitSize === "2"}
                      onChange={(e) => setCfbBitSize(e.target.value)}
                      className="form-radio text-primary_2 focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="text-white ml-2">2 bit</span>
                  </label>
                  <label className="flex items-center">
                    <input
                      type="radio"
                      value="4"
                      checked={cfbBitSize === "4"}
                      onChange={(e) => setCfbBitSize(e.target.value)}
                      className="form-radio text-primary_2 focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="text-white ml-2">4 bit</span>
                  </label>
                  <label className="flex items-center">
                    <input
                      type="radio"
                      value="8"
                      checked={cfbBitSize === "8"}
                      onChange={(e) => setCfbBitSize(e.target.value)}
                      className="form-radio text-primary_2 focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="text-white ml-2">8 bit</span>
                  </label>
                </div>
              </div>
            )}


            {encryptionMode === "ofb" && (
              <div className="mb-4">
                <h2 className="h-8 items-center ml-1 mt-4 flex text-lg font-semibold text-white">Select OFB Bit Size:</h2>
                <div className="flex items-center space-x-4">
                  <label className="flex items-center">
                    <input
                      type="radio"
                      value="2"
                      checked={ofbBitSize === "2"}
                      onChange={(e) => setOfbBitSize(e.target.value)}
                      className="form-radio text-primary_2 focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="text-white ml-2">2 bit</span>
                  </label>
                  <label className="flex items-center">
                    <input
                      type="radio"
                      value="4"
                      checked={ofbBitSize === "4"}
                      onChange={(e) => setOfbBitSize(e.target.value)}
                      className="form-radio text-primary_2 focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="text-white ml-2">4 bit</span>
                  </label>
                  <label className="flex items-center">
                    <input
                      type="radio"
                      value="8"
                      checked={ofbBitSize === "8"}
                      onChange={(e) => setOfbBitSize(e.target.value)}
                      className="form-radio text-primary_2 focus:ring-2 focus:ring-blue-500"
                    />
                    <span className="text-white ml-2">8 bit</span>
                  </label>
                </div>
              </div>
            )}

            {/* Select Mode */}


            <h2 className="h-8 items-center ml-1 mb-2 flex text-lg font-semibold text-white">
              Key
            </h2>
            <div className="flex-col mx-1 mb-3">
              <input
                id="key"
                className="w-full p-1.5 text-lg text-white bg-primary_2 rounded-md border border-primary_3 focus:ring-blue-50 mr-2"
                placeholder="Key"
                value={key}
                onChange={(e) => setKey(e.target.value)}
              ></input>
            </div>
            <div className="lg:flex">
              <button
                onClick={encryptAction}
                className="bg-primary_2 hover:bg-primary_3 border-primary_3 text-secondary px-2 py-1.5 my-1 lg:mr-1 rounded flex items-center mx-auto"
              >
                <MdLockOutline size="16" />
                <span className="text-sm">Encrypt</span>
              </button>
              <button
                onClick={decryptAction}
                className="bg-primary_2 hover:bg-primary_3 border-primary_3 text-secondary px-2 py-1.5 my-1 lg:ml-1 rounded flex items-center mx-auto"
              >
                <MdLockOpen size="16" />
                <span className="text-sm">Decrypt</span>
              </button>
            </div>
          </div>

          {/* output */}
          <div className="basis-5/12 flex-col mx-1">
            <h2 className="h-8 items-center ml-1 mb-2 flex text-lg font-semibold text-white">
              Output
            </h2>
            <textarea
              readOnly
              id="output"
              ref={outputTextArea}
              rows="8"
              className="w-full p-2 text-lg text-white bg-primary_2 rounded-md border border-primary_3"
              value={userOutput}
            ></textarea>
            <div className="flex justify-end">
              {/* download as txt file */}
              <FileOutput
                handleOnChangeParent={handleFileOutputChange}
                handleOnSubmitParent={handleFileOutputSubmit}
              />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Delazi;
