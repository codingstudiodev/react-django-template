import { Suspense } from 'react'
import { Provider } from 'react-redux'
import { BrowserRouter } from 'react-router-dom'
import { PersistGate } from 'redux-persist/integration/react'

import { store, persistor } from './app/store'
import AppRouter from './routers/AppRouter'

function App() {
	return (
		<Provider store={store}>
			<PersistGate loading={<></>} persistor={persistor}>
				<Suspense>
					<BrowserRouter>
						<AppRouter />
					</BrowserRouter>
				</Suspense>
			</PersistGate>
		</Provider>
	)
}

export default App
