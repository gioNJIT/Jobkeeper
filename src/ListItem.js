import React from 'react';
import PropTypes from 'prop-types';

export function ListItem(props) {
  const { name } = props;
  return <div><center>{ name }</center></div>;
}
ListItem.propTypes = {
  name: PropTypes.string,
};

ListItem.defaultProps = {
  name: PropTypes.string,
};
export default ListItem;
