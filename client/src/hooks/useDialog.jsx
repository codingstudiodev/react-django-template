import { useState } from 'react'
import PropTypes from 'prop-types'

/**
 * @typedef {Object} DialogState
 */

/**
 * @typedef {import('react').Dispatch<import('react').SetStateAction<DialogState>>} SetDialogState
 */

/**
 * Hook personalizado para el manejo de diálogos.
 * @param {DialogState} initState - Estado inicial del diálogo.
 * @returns {[DialogState, SetDialogState]} - Estado actual y función para actualizar el estado.
 */

const useDialog = initState => {
	const [showDialog, setShowDialog] = useState(initState)

	/**
	 * Función para cambiar el estado del diálogo.
	 * @param {keyof DialogState} name - Nombre del diálogo a cambiar.
	 * @param {boolean} value - Nuevo valor para el diálogo.
	 */

	const changeDialog = (name, value) => {
		setShowDialog(current => ({
			...current,
			[name]: value,
		}))
	}

	return [showDialog, changeDialog]
}

useDialog.propTypes = {
	initState: PropTypes.object.isRequired,
}

export default useDialog
