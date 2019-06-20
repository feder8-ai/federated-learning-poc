import green from "@material-ui/core/colors/green";

const styles = theme => ({
    container: {
        padding: 24
    },
    textField: {
        marginLeft: theme.spacing.unit,
        marginRight: theme.spacing.unit,
        width: 500,
    },
      formControl: {
        margin: theme.spacing.unit,
        minWidth: 120,
    },
    wrapper: {
      margin: theme.spacing.unit,
      position: 'relative',
    },
    buttonSuccess: {
      backgroundColor: green[500],
      '&:hover': {
        backgroundColor: green[700],
      },
    },
    fabProgress: {
      color: green[500],
      position: 'absolute',
      top: -6,
      left: -6,
      zIndex: 1,
    },
    buttonProgress: {
      color: green[500],
      position: 'absolute',
      top: '50%',
      left: '50%',
      marginTop: -12,
      marginLeft: -12,
    },
     input: {
      display: 'none',
    },
});

export default styles;