import path from 'path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
	resolve: {
		alias: [
			{
				find: '@api',
				replacement: path.resolve(__dirname, './client/src/api'),
			},
			{
				find: '@assets',
				replacement: path.resolve(__dirname, './client/src/assets'),
			},
			{
				find: '@components',
				replacement: path.resolve(__dirname, './client/src/components'),
			},
			{
				find: '@routes',
				replacement: path.resolve(__dirname, './client/src/helpers/routes.js'),
			},
			{
				find: '@choices',
				replacement: path.resolve(__dirname, './client/src/helpers/choices'),
			},
			{
				find: '@hooks',
				replacement: path.resolve(__dirname, './client/src/hooks'),
			},
			{
				find: '@pages',
				replacement: path.resolve(__dirname, './client/src/pages'),
			},
			{
				find: '@services',
				replacement: path.resolve(__dirname, './client/src/services'),
			},
			{
				find: '@styles',
				replacement: path.resolve(__dirname, './client/src/styles'),
			},
			{
				find: '@utilities',
				replacement: path.resolve(__dirname, './client/src/utilities'),
			},
		],
		extensions: ['.js', '.json', '.jsx', '.ts', '.tsx'],
	},
	mode: 'production',
	publicDir: path.resolve(__dirname, './client/public/'),
	root: path.resolve(__dirname, './client/'),
	build: { outDir: path.resolve(__dirname, 'dist'), emptyOutDir: true },
	plugins: [react()],
})
