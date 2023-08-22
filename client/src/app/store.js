import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query'
import { apiSlice, apiSliceWithRefresh } from '../api/apiSlice'
import { authApiSlice, registerApiSlice } from '../services'
import { auth, meta } from './states'

import storage from 'redux-persist/lib/storage'
import { persistReducer, persistStore, PURGE } from 'redux-persist'

const persistConfig = {
	key: 'root',
	storage,
}

const persistedReducer = persistReducer(persistConfig, auth)

export const store = configureStore({
	reducer: {
		[authApiSlice.reducerPath]: authApiSlice.reducer,
		[registerApiSlice.reducerPath]: registerApiSlice.reducer,
		auth: persistedReducer,
		meta,
	},
	extraReducers: builder => {
		builder.addCase(PURGE, () => {
			storage.removeAll('root')
		})
	},
	middleware: gDM =>
		gDM({
			thunk: {
				extraArgument: apiSlice.middleware,
			},
			serializableCheck: false,
		}).concat([apiSlice.middleware, apiSliceWithRefresh.middleware, authApiSlice.middleware]),
	devTools: true,
})

setupListeners(store.dispatch)

export const persistor = persistStore(store)
