import { createSlice } from '@reduxjs/toolkit'

const initialState = {
	title: '',
	alert: {
		message: '',
		type: 'alert-success',
		show: false,
	},
	breadcrumb: () => <li className='breadcrumb-item active'>Inicio</li>,
}

const metaSlice = createSlice({
	name: 'meta',
	initialState,
	reducers: {
		setTitle: (state, action) => {
			state.title = action.payload
		},
		setBreadcrumb: (state, action) => {
			state.breadcrumb = action.payload
		},
		setAlert: (state, action) => {
			state.alert = action.payload
		},
	},
})

export const { setAlert, setTitle, setBreadcrumb } = metaSlice.actions

export default metaSlice.reducer

export const selectCurrentTitle = state => state.meta.title
export const selectCurrentBreadcrumb = state => state.meta.breadcrumb
export const selectCurrentAlert = state => state.meta.alert
