import PropTypes from "prop-types";

const TextInput = ({ handleOnChangeParent, text }) => {
  const handleOnChange = (e) => {
    handleOnChangeParent(e.target.value);
  };

  return (
    <textarea
      id="input"
      rows="8"
      className="w-full p-2 text-lg text-white bg-primary_2 rounded-md border border-primary_3 focus:ring-blue-50"
      placeholder="Write plaintext here..."
      value={text}
      onChange={handleOnChange}
    ></textarea>
  );
};

export default TextInput;

TextInput.propTypes = {
  handleOnChangeParent: PropTypes.func.isRequired,
  text: PropTypes.string,
};
