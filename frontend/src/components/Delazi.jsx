import { useState, useRef } from "react";
import { MdLockOutline, MdLockOpen, MdArrowCircleLeft } from "react-icons/md";
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

  const [key, setKey] = useState("");

  const [mode, setMode] = useState("ecb");
  const [keyLength, setKeyLength] = useState(128);
  const [round, setRound] = useState(10);
  const [size, setSize] = useState(2);
  const [time, setTime] = useState(0);

  const setInputAsOutput = () => {
    setUserInput(userOutput);
  };

  const validateKey = () => {
    let errorMessage = "";
    if (keyLength === 128 && key.length !== 16) {
      errorMessage = "Key length should be 16 characters for 128-bit key.";
    } else if (keyLength === 192 && key.length !== 24) {
      errorMessage = "Key length should be 24 characters for 192-bit key.";
    } else if (keyLength === 256 && key.length !== 32) {
      errorMessage = "Key length should be 32 characters for 256-bit key.";
    }
    return errorMessage;
  };

  const showAlert = (message) => {
    alert(message);
  };

  const handleFormat = (format) => {
    setFormat(format);
  };

  const handleKeyLengthChange = (event) => {
    const keyLength = parseInt(event.target.value);
    setKeyLength(keyLength);
    if (keyLength === 128) {
      setRound(10);
    } else if (keyLength === 192) {
      setRound(12);
    }
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
    const errorMessage = validateKey();
    if (errorMessage) {
      showAlert(errorMessage);
      return;
    }

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
          plaintext: stringToHex(userInput),
          key: key,
          round: round,
          mode: mode,
          ...((mode === "cfb" || mode === "ofb") && { size: size }),
        }),
      });

      const data = await response.json();
      if (data.status != 200) {
        setUserOutput("Error encrypting message.");
        return;
      }
      const encrypted = hexToString(data.message.encrypted);
      setUserOutput(encrypted);
      const time = parseFloat(data.message.time);
      setTime(parseFloat(time.toFixed(3)));
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
      formData.append("round", round);
      formData.append("mode", mode);
      if (mode === "cfb" || mode === "ofb") {
        formData.append("size", size);
      }

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

      const time = parseFloat(response.headers.get("time"));
      setTime(parseFloat(time.toFixed(3)));

      const reader = new FileReader();
      reader.onload = function (event) {
        setUserOutput(event.target.result);
      };

      reader.readAsText(blob, "ASCII");
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error downloading file.");
    }
  };

  const decryptAction = async () => {
    const errorMessage = validateKey();
    if (errorMessage) {
      showAlert(errorMessage);
      return;
    }

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
          ciphertext: stringToHex(userInput),
          key: key,
          round: round,
          mode: mode,
          ...((mode === "cfb" || mode === "ofb") && { size: size }),
        }),
      });

      const data = await response.json();
      if (data.status != 200) {
        setUserOutput("Error encrypting message.");
        return;
      }
      const decrypted = hexToString(data.message.decrypted);
      setUserOutput(decrypted);
      const time = parseFloat(data.message.time);
      setTime(parseFloat(time.toFixed(3)));
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
      formData.append("round", round);
      formData.append("mode", mode);
      if (mode === "cfb" || mode === "ofb") {
        formData.append("size", size);
      }

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

      const time = parseFloat(response.headers.get("time"));
      setTime(parseFloat(time.toFixed(3)));

      const reader = new FileReader();
      reader.onload = function (event) {
        setUserOutput(event.target.result);
      };

      reader.readAsText(blob, "ASCII");
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error downloading file.");
    }
  };

  const handleFileOutputSubmit = () => {
    const element = document.createElement("a");

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
            <h2 className="h-8 items-center mx-1 mb-2 flex text-lg font-semibold text-white">
              Input
            </h2>
            {/* text input */}
            {format === "text" && (
              <TextInput
                text={userInput}
                handleOnChangeParent={handleUserInput}
              />
            )}

            {/* file input */}
            {format === "file" && (
              <FileInput
                handleOnChangeParent={handleFileInputChange}
                fileName={fileInputName}
              />
            )}

            <h2 className="h-8 items-center mx-1 mb-1 flex text-lg font-semibold text-white">
              Mode
            </h2>
            {/* mode picker */}
            <ul className="lg:flex items-center text-white bg-primary_2 rounded-md border border-primary_3 focus:ring-blue-50">
              <li className="w-full lg:border-r border-b border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="list-ecb"
                    type="radio"
                    value="ecb"
                    className="w-4"
                    checked={mode === "ecb"}
                    onChange={(e) => setMode(e.target.value)}
                  />
                  <label htmlFor="list-ecb" className="w-full ms-2 text-sm">
                    ECB
                  </label>
                </div>
              </li>
              <li className="w-full lg:border-r border-b border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="list-cbc"
                    type="radio"
                    value="cbc"
                    className="w-4"
                    checked={mode === "cbc"}
                    onChange={(e) => setMode(e.target.value)}
                  />
                  <label htmlFor="list-cbc" className="w-full ms-2 text-sm">
                    CBC
                  </label>
                </div>
              </li>
              <li className="w-full lg:border-r border-b border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="list-ofb"
                    type="radio"
                    value="ofb"
                    className="w-4"
                    checked={mode === "ofb"}
                    onChange={(e) => setMode(e.target.value)}
                  />
                  <label htmlFor="list-ofb" className="w-full ms-2 text-sm">
                    OFB
                  </label>
                </div>
              </li>
              <li className="w-full lg:border-r border-b border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="list-cfb"
                    type="radio"
                    value="cfb"
                    className="w-4"
                    checked={mode === "cfb"}
                    onChange={(e) => setMode(e.target.value)}
                  />
                  <label htmlFor="list-cfb" className="w-full ms-2 text-sm">
                    CFB
                  </label>
                </div>
              </li>
              <li className="w-full">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="list-ctr"
                    type="radio"
                    value="counter"
                    className="w-4"
                    checked={mode === "counter"}
                    onChange={(e) => setMode(e.target.value)}
                  />
                  <label htmlFor="list-ctr" className="w-full ms-2 text-sm">
                    Counter
                  </label>
                </div>
              </li>
            </ul>
          </div>

          {/* settings */}
          <div className="basis-2/12 flex-col mx-1">
            <h2 className="h-8 items-center flex text-lg font-semibold text-white">
              Settings
            </h2>

            {/* Select Key Length */}
            <h3 className="h-14 lg:h-8 items-center mx-1 flex text-md text-white">
              Key Bit Size
            </h3>

            <ul className="lg:flex text-white bg-primary_2 mb-2 rounded-md border border-primary_3">
              <li className="w-full lg:border-r border-b border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="key-128"
                    type="radio"
                    value={128}
                    checked={keyLength === 128}
                    onChange={handleKeyLengthChange}
                  />
                  <label htmlFor="key-128" className="w-full ms-2 text-sm">
                    128
                  </label>
                </div>
              </li>
              <li className="w-full lg:border-r border-b border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="key-192"
                    type="radio"
                    value={192}
                    checked={keyLength === 192}
                    onChange={handleKeyLengthChange}
                  />
                  <label htmlFor="key-192" className="w-full ms-2 text-sm">
                    192
                  </label>
                </div>
              </li>
              <li className="w-full border-primary_3">
                <div className="flex items-center px-3 h-8">
                  <input
                    id="key-256"
                    type="radio"
                    value={256}
                    checked={keyLength === 256}
                    onChange={handleKeyLengthChange}
                  />
                  <label htmlFor="key-256" className="w-full ms-2 text-sm">
                    256
                  </label>
                </div>
              </li>
            </ul>

            {/* Select Rounds for 256-bit Key */}
            {keyLength === 256 && (
              <>
                <h3 className="h-8 items-center mx-1 flex text-md text-white">
                  Round
                </h3>
                <ul className="lg:flex text-white bg-primary_2 mb-2 rounded-md border border-primary_3">
                  <li className="w-full border-b lg:border-r border-primary_3">
                    <div className="flex items-center px-3 h-8">
                      <input
                        id="round-14"
                        type="radio"
                        value={14}
                        checked={round === 14}
                        onChange={(e) => setRound(parseInt(e.target.value))}
                      />
                      <label htmlFor="round-14" className="w-full ms-2 text-sm">
                        14
                      </label>
                    </div>
                  </li>
                  <li className="w-full border-b lg:border-r border-primary_3">
                    <div className="flex items-center px-3 h-8">
                      <input
                        id="round-16"
                        type="radio"
                        value={16}
                        checked={round === 16}
                        onChange={(e) => setRound(parseInt(e.target.value))}
                      />
                      <label htmlFor="round-16" className="w-full ms-2 text-sm">
                        16
                      </label>
                    </div>
                  </li>
                </ul>
              </>
            )}

            {/* key */}
            <h3 className="h-8 items-center mx-1 flex text-md text-white">
              Key
            </h3>
            <textarea
              id="key"
              rows="2"
              className="w-full p-1.5 text-lg text-white bg-primary_2 rounded-md border border-primary_3 focus:ring-blue-50"
              placeholder="Write key here..."
              value={key}
              onChange={(e) => setKey(e.target.value)}
            ></textarea>

            {/* byte size picker */}
            {(mode === "cfb" || mode === "ofb") && (
              <>
                <h3 className="h-14 lg:h-8 items-center mx-1 flex text-md text-white">
                  OFB/CFB Byte Size
                </h3>

                <ul className="lg:flex text-white bg-primary_2 mb-2 rounded-md border border-primary_3">
                  <li className="w-full border-b lg:border-r border-primary_3">
                    <div className="flex items-center px-3 h-8">
                      <input
                        id="size-2"
                        type="radio"
                        value={2}
                        checked={size === 2}
                        onChange={(e) => setSize(parseInt(e.target.value))}
                      />
                      <label htmlFor="size-2" className="w-full ms-2 text-sm">
                        2B
                      </label>
                    </div>
                  </li>
                  <li className="w-full border-b lg:border-r border-primary_3">
                    <div className="flex items-center px-3 h-8">
                      <input
                        id="size-4"
                        type="radio"
                        value={4}
                        checked={size === 4}
                        onChange={(e) => setSize(parseInt(e.target.value))}
                      />
                      <label htmlFor="size-4" className="w-full ms-2 text-sm">
                        4B
                      </label>
                    </div>
                  </li>
                  <li className="w-full border-primary_3">
                    <div className="flex items-center px-3 h-8">
                      <input
                        id="size-8"
                        type="radio"
                        value={8}
                        checked={size === 8}
                        onChange={(e) => setSize(parseInt(e.target.value))}
                      />
                      <label htmlFor="size-8" className="w-full ms-2 text-sm">
                        8B
                      </label>
                    </div>
                  </li>
                </ul>
              </>
            )}

            <div className="lg:flex mb-3">
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
            <button
              onClick={setInputAsOutput}
              className="rounded-full flex items-center justify-center w-8 h-8 border border-primary_3 mx-auto mt-3"
            >
              <MdArrowCircleLeft size="24" />
            </button>
          </div>

          {/* output */}
          <div className="basis-5/12 flex-col mx-1">
            <h2 className="h-8 items-center mx-1 mb-2 flex text-lg font-semibold text-white">
              Output
            </h2>
            <textarea
              readOnly
              id="output"
              ref={outputTextArea}
              rows="8"
              className="mb-2 w-full p-2 text-lg text-white bg-primary_2 rounded-md border border-primary_3"
              value={userOutput}
            ></textarea>
            <div className="flex justify-between">
              <div className="lg:flex h-12 mr-6">
                <h2 className="items-center ml-1 flex text-lg font-semibold text-white">
                  Time:
                </h2>
                <p className="flex text-white items-center text-lg ml-1 leading-4">
                  {time} s
                </p>
              </div>
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
